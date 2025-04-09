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
        console.error('Sending error', error);
        return throwError(() => new Error('Try again'));
      })
    );
  }
}
