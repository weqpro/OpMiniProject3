import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Volonteer } from '../schemas/volonteer';
import { Observable, catchError, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class VolonteerService {
  private http = inject(HttpClient);
  private apiUrl = 'http://127.0.0.1:8000/api/v1/volunteers';

  create(volonteer: Volonteer): Observable<any> {
    return this.http.post('http://127.0.0.1:8000/api/v1/auth/register/volunteer', volonteer).pipe(
      catchError((error) => {
        console.error('Error creating volonteer:', error);
        return throwError(() => new Error('Could not create volonteer. Please try again.'));
      })
    );
  }
  getById(id: number): Observable<Volonteer> {
    return this.http.get<Volonteer>(`${this.apiUrl}/${id}`).pipe(
      catchError((error) => {
        console.error(`Error fetching volonteer with ID ${id}:`, error);
        return throwError(() => new Error('Could not fetch volonteer. Please try again.'));
      })
    );
  }
  delete(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`).pipe(
      catchError((error) => {
        console.error(`Error deleting volonteer with ID ${id}:`, error);
        return throwError(() => new Error('Could not delete volonteer. Please try again.'));
      })
    );
  }
  getProfile(): Observable<any> {
    return this.http.get(`${this.apiUrl}/me`);
  }

  updateProfile(data: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/me`, data);
  }

  changePassword(payload: { current_password: string; new_password: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/change-password`, payload);
  }

  deleteAccount(): Observable<any> {
    return this.http.delete('http://127.0.0.1:8000/api/v1/volunteers/me');
  }
  getSoldierById(id: number): Observable<any> {
    return this.http.get(`http://127.0.0.1:8000/api/v1/soldiers/${id}`);
  }

}