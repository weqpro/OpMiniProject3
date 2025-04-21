import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Soldier } from '../schemas/soldier';
import { Observable, catchError, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SoldierService {
  private http = inject(HttpClient);
  private apiUrl = 'https://your-api.com/soldiers';

  create(soldier: Soldier): Observable<any> {
    return this.http.post(this.apiUrl, soldier).pipe(
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
    return this.http.get(`https://your-api.com/soldier/me`);
  }

  updateProfile(data: any): Observable<any> {
    return this.http.put(`https://your-api.com/soldier/me`, data);
  }

  changePassword(payload: { current_password: string; new_password: string }): Observable<any> {
    return this.http.post('/api/v1/soldiers/change-password', payload);
  }

}