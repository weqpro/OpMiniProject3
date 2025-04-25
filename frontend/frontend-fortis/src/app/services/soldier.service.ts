import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Soldier } from '../schemas/soldier';
import { Observable, catchError, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SoldierService {
  private http = inject(HttpClient);
  private apiUrl = 'http://127.0.0.1:8000/api/v1/soldiers';

  create(soldier: Soldier): Observable<any> {
    return this.http.post("http://127.0.0.1:8000/api/v1/auth/register/soldier", soldier).pipe(
      catchError((error) => {
        console.error('Error creating soldier:', error);
        return throwError(() => new Error('Could not create soldier. Please try again.'));
      })
    );
  }
  getById(id: number): Observable<Soldier> {
    return this.http.get<Soldier>(`${this.apiUrl}/${id}`).pipe(
      catchError((error) => {
        console.error(`Error fetching soldier with ID ${id}:`, error);
        return throwError(() => new Error('Could not fetch soldier. Please try again.'));
      })
    );
  }
  delete(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`).pipe(
      catchError((error) => {
        console.error(`Error deleting soldier with ID ${id}:`, error);
        return throwError(() => new Error('Could not delete soldier. Please try again.'));
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
    return this.http.delete('http://127.0.0.1:8000/api/v1/soldiers/me');
  }

  getSoldierById(id: number): Observable<any> {
    return this.http.get(`http://127.0.0.1:8000/api/v1/soldiers/soldier-info/${id}`);
  }

}
