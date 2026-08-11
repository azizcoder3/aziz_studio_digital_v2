/* ==========================================================================
   MODULE COMMANDE JS (SPRINT 40)
   Aziz Studio Digital V2 - Gestion dynamique des paramètres d'offre
   ========================================================================== */

document.addEventListener('DOMContentLoaded', function() {
    const params = new URLSearchParams(window.location.search);
    
    const secteur = params.get('secteur');
    const offre = params.get('offre');
    const prix = params.get('prix');

    const summaryTitleEl = document.getElementById('summary-offre-title');
    const summaryPriceEl = document.getElementById('summary-offre-price');
    const hiddenSecteurEl = document.getElementById('secteur_origine');
    const formHeadingEl = document.getElementById('commande-form-subtitle');

    if (offre && summaryTitleEl) {
        summaryTitleEl.textContent = offre;
    }

    if (prix && summaryPriceEl) {
        summaryPriceEl.textContent = 'À partir de ' + prix;
    }

    if (secteur && hiddenSecteurEl) {
        hiddenSecteurEl.value = secteur + ' - ' + (offre || '');
    }

    if (offre && formHeadingEl) {
        formHeadingEl.textContent = 'Complétez le formulaire ci-dessous pour recevoir votre proposition personnalisée pour la formule "' + offre + '".';
    }
});
