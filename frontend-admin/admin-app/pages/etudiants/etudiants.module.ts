import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EtudiantsComponent } from './etudiants.component';

@NgModule({
  declarations: [EtudiantsComponent],
  imports: [CommonModule],
  exports: [EtudiantsComponent]
})
export class EtudiantsModule {}
