import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Volonteer } from '../schemas/volonteer';
import { Soldier } from '../schemas/soldier';
import { Observable, catchError, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private http = inject(HttpClient);

  private volonteerUrl = '#';
  private soldierUrl = '#';

  createVolonteer(volonteer: Volonteer): Observable<any> {
    return this.http.post(this.volonteerUrl, volonteer).pipe(
      catchError(this.handleError('create volonteer'))
    );
  }

  createSoldier(soldier: Soldier): Observable<any> {
    return this.http.post(this.soldierUrl, soldier).pipe(
      catchError(this.handleError('create soldier'))
    );
  }

  private handleError(action: string) {
    return (error: any) => {
      console.error(`Failed to ${action}:`, error);
      return throwError(() => new Error(`An error occurred while trying to ${action}. Please try again later.`));
    };
  }
}
