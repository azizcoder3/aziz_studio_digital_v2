const nodemailer = require('nodemailer');

exports.handler = async function(event, context) {
    // Only respond to POST requests to avoid errors on accidental GET
    if (event.httpMethod !== 'POST') {
        return { statusCode: 200, body: 'Method Not Allowed' };
    }

    // 0. Vérification de sécurité : secret partagé (Header HTTP ou Query Parameter)
    // Permet de s'assurer que la requête provient bien de notre Webhook Netlify
    const expectedSecret = process.env.WEBHOOK_SECRET;
    if (expectedSecret) {
        const headers = event.headers || {};
        const incomingHeaderSecret = headers['x-webhook-secret'] || headers['X-Webhook-Secret'];
        const queryParams = event.queryStringParameters || {};
        const incomingQuerySecret = queryParams.secret;

        const providedSecret = incomingHeaderSecret || incomingQuerySecret;

        if (!providedSecret || providedSecret !== expectedSecret) {
            console.warn("Accès non autorisé : secret Webhook absent ou invalide.");
            return { statusCode: 200, body: 'Unauthorized' };
        }
    }

    try {
        const body = JSON.parse(event.body);
        
        // Netlify Forms Outgoing Webhook structure
        const payload = body.payload || body;
        const data = payload.data || payload;
        
        // 1. Vérification du honeypot
        const honeypot = data['bot-field'] || data['bot_field'];
        if (honeypot) {
            console.warn("Honeypot rempli, abandon silencieux de l'envoi.");
            // On retourne toujours 200 pour que le webhook Netlify soit considéré comme réussi
            return { statusCode: 200, body: "Spam detected" };
        }

        // 2. Extraction des champs
        const formName = payload.form_name || data['form-name'] || data['form_name'];
        const userEmail = data.email;
        const userNom = data.nom || "";
        const userPrenom = data.prenom || "";

        if (!userEmail) {
            console.warn("Aucun email fourni, abandon silencieux de l'envoi.");
            return { statusCode: 200, body: "No email" };
        }

        // 3. Configuration de Nodemailer (utilisation stricte des variables d'environnement)
        const transporter = nodemailer.createTransport({
            host: 'smtp.gmail.com',
            port: 465,
            secure: true,
            auth: {
                user: process.env.GMAIL_USER,
                pass: process.env.GMAIL_APP_PASSWORD
            }
        });

        let subject = "";
        let htmlBody = "";

        // 4. Sélection du template
        if (formName === 'commande') {
            const offre = data.offre || "Sur-Mesure";
            subject = `Votre demande d'offre ${offre} — Aziz Studio Digital`;
            htmlBody = `
            <div style="font-family: 'Helvetica Neue', Arial, sans-serif; max-width: 600px; margin: 0 auto; color: #333333; line-height: 1.6;">
                <h2 style="color: #6C5CE7; font-size: 24px; margin-bottom: 24px;">Aziz <strong style="font-weight: 800;">Studio</strong> Digital</h2>
                
                <p>Bonjour ${userPrenom} ${userNom},</p>
                
                <p>Nous avons bien reçu votre demande concernant l'offre <strong>${offre}</strong> et nous vous remercions de votre confiance.</p>
                
                <p>Notre équipe étudie actuellement les détails de votre projet. Nous reviendrons vers vous sous <strong>72 heures</strong> avec une proposition adaptée et un devis sans engagement.</p>
                
                <p>Si vous souhaitez nous apporter des précisions supplémentaires, vous pouvez répondre directement à cet email.</p>
                
                <br>
                <p>Cordialement,</p>
                <p><strong>L'équipe Aziz Studio Digital</strong></p>
                
                <hr style="border: none; border-top: 1px solid #eeeeee; margin: 32px 0;">
                
                <p style="font-size: 0.9em; color: #777777;">
                    📧 azizstudio.dev@gmail.com<br>
                    📍 République du Congo<br>
                </p>
            </div>
            `;
        } else {
            // Template par défaut (formulaire 'contact' ou autre)
            const typeProjet = data.type_projet || "projet web";
            subject = `Votre message a bien été reçu — Aziz Studio Digital`;
            htmlBody = `
            <div style="font-family: 'Helvetica Neue', Arial, sans-serif; max-width: 600px; margin: 0 auto; color: #333333; line-height: 1.6;">
                <h2 style="color: #6C5CE7; font-size: 24px; margin-bottom: 24px;">Aziz <strong style="font-weight: 800;">Studio</strong> Digital</h2>
                
                <p>Bonjour ${userPrenom} ${userNom},</p>
                
                <p>Nous avons bien reçu votre message concernant votre <strong>${typeProjet}</strong> et nous vous en remercions.</p>
                
                <p>Nous prendrons connaissance de votre demande dans les plus brefs délais. Vous recevrez une réponse personnalisée de notre part sous <strong>72 heures</strong> maximum.</p>
                
                <p>Si votre demande est urgente, n'hésitez pas à nous recontacter par retour d'email ou via nos canaux habituels.</p>
                
                <br>
                <p>Cordialement,</p>
                <p><strong>L'équipe Aziz Studio Digital</strong></p>
                
                <hr style="border: none; border-top: 1px solid #eeeeee; margin: 32px 0;">
                
                <p style="font-size: 0.9em; color: #777777;">
                    📧 azizstudio.dev@gmail.com<br>
                    📍 République du Congo<br>
                </p>
            </div>
            `;
        }

        const mailOptions = {
            from: `"Aziz Studio Digital" <${process.env.GMAIL_USER}>`,
            to: userEmail,
            subject: subject,
            html: htmlBody
        };

        // 5. Envoi
        await transporter.sendMail(mailOptions);
        
        return {
            statusCode: 200,
            body: JSON.stringify({ message: "Email de confirmation envoyé avec succès." })
        };

    } catch (error) {
        // En cas d'erreur (ex: problème SMTP, identifiants incorrects), on log discrètement sans exposer les variables.
        // On retourne toujours 200 pour que l'utilisateur final ne voie pas d'erreur sur le site, 
        // puisque le formulaire Netlify est quand même enregistré.
        console.error("Erreur lors de l'envoi de l'autoreply (SMTP ou parse):", error.message);
        return {
            statusCode: 200,
            body: JSON.stringify({ message: "La soumission a été reçue mais l'email de confirmation a échoué." })
        };
    }
};
