import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Formation {
  id: number;
  titre: string;
  description?: string;
  theme?: string;
  duree?: number;
}

@Injectable({ providedIn: 'root' })
export class FormationsService {
  private apiUrl = 'http://localhost:8000/formations';

  constructor(private http: HttpClient) {}

  getFormations(): Observable<Formation[]> {
    return this.http.get<Formation[]>(this.apiUrl);
  }

  getFormation(id: number): Observable<Formation> {
    return this.http.get<Formation>(`${this.apiUrl}/${id}`);
  }

  addFormation(formation: Partial<Formation>): Observable<Formation> {
    return this.http.post<Formation>(this.apiUrl, formation);
  }

  updateFormation(id: number, formation: Partial<Formation>): Observable<Formation> {
    return this.http.put<Formation>(`${this.apiUrl}/${id}`, formation);
  }

  deleteFormation(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`);
  }
}
