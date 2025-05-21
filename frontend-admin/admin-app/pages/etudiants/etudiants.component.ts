import { Component, OnInit } from '@angular/core';
import { EtudiantsService, Etudiant } from './etudiants.service';

@Component({
  selector: 'app-etudiants',
  templateUrl: './etudiants.component.html',
})
export class EtudiantsComponent implements OnInit {
  etudiants: Etudiant[] = [];
  loading = true;

  constructor(private etudiantsService: EtudiantsService) {}

  ngOnInit() {
    this.etudiantsService.getEtudiants().subscribe({
      next: (data) => {
        this.etudiants = data;
        this.loading = false;
      },
      error: () => {
        this.loading = false;
      }
    });
  }
}
