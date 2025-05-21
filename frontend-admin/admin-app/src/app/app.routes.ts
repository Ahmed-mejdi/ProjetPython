import { Routes } from '@angular/router';

export const routes: Routes = [
  // Dashboard admin
  { path: 'dashboard', loadChildren: () => import('./pages/dashboard/dashboard.module').then(m => m.DashboardModule) },
  // Gestion étudiants
  { path: 'etudiants', loadChildren: () => import('./pages/etudiants/etudiants.module').then(m => m.EtudiantsModule) },
  // Gestion formations
  { path: 'formations', loadChildren: () => import('./pages/formations/formations.module').then(m => m.FormationsModule) },
  // Statistiques
  { path: 'statistiques', loadChildren: () => import('./pages/statistiques/statistiques.module').then(m => m.StatistiquesModule) },
  // Page d'accueil par défaut
  { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
];
