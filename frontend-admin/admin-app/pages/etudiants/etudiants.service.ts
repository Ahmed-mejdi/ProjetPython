import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Etudiant {
  id: number;
  nom: string;
  email: string;
  departement_id?: number;
}

@Injectable({ providedIn: 'root' })
export class EtudiantsService {
  private apiUrl = 'http://localhost:8000/etudiants';

  constructor(private http: HttpClient) {}

  getEtudiants(): Observable<Etudiant[]> {
    return this.http.get<Etudiant[]>(this.apiUrl);
  }

  getEtudiant(id: number): Observable<Etudiant> {
    return this.http.get<Etudiant>(`${this.apiUrl}/${id}`);
  }

  addEtudiant(etudiant: Partial<Etudiant>): Observable<Etudiant> {
    return this.http.post<Etudiant>(this.apiUrl, etudiant);
  }

  updateEtudiant(id: number, etudiant: Partial<Etudiant>): Observable<Etudiant> {
    return this.http.put<Etudiant>(`${this.apiUrl}/${id}`, etudiant);
  }

  deleteEtudiant(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`);
  }
}
