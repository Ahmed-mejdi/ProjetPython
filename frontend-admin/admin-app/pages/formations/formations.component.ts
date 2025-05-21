import { Component, OnInit } from '@angular/core';
import { FormationsService, Formation } from './formations.service';

@Component({
  selector: 'app-formations',
  templateUrl: './formations.component.html',
})
export class FormationsComponent implements OnInit {
  formations: Formation[] = [];
  loading = true;

  constructor(private formationsService: FormationsService) {}

  ngOnInit() {
    this.formationsService.getFormations().subscribe({
      next: (data) => {
        this.formations = data;
        this.loading = false;
      },
      error: () => {
        this.loading = false;
      }
    });
  }
}
