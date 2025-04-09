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
}
