import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, throwError } from 'rxjs';
import { Volonteer } from '../schemas/volonteer';

@Injectable({
  providedIn: 'root'
})
export class VolonteerService {
  private http = inject(HttpClient);
  private apiUrl = 'https://your-api.com/volunteers';

  create(volonteer: Volonteer): Observable<any> {
    return this.http.post(this.apiUrl, volonteer).pipe(
      catchError((error) => {
        console.error('Sending erroe', error);
        return throwError(() => new Error('Try again'));
      })
    );
  }
}
