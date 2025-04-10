import {inject, Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable, throwError} from 'rxjs';
import {SearchOptions} from '../schemas/search-options';
import {AidRequest} from '../schemas/aid-request';
import {catchError} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AidRequestService {
  private http = inject(HttpClient);
  private apiUrl = '#'
  constructor() { }

  private handleError(error: HttpErrorResponse) {
    if (error.status === 0) {
      console.error('An error occurred:', error.error);
    } else {
      console.error(
        `Backend returned code ${error.status}, body was: `, error.error);
    }
    return throwError(() => new Error('Something bad happened; please try again later.'));
  }

  search(options: SearchOptions): Observable<AidRequest[]> {
    return this.http.post<AidRequest[]>(this.apiUrl, options);
  }

  getAllRequests(): Observable<any> {
    return this.http.get(this.apiUrl);
  }

  createRequest(data: AidRequest): Observable<any> {
    return this.http.post(this.apiUrl, data);
  }

  deleteRequest(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`);
  }

  publishRequest(id: number): Observable<AidRequest> {
    return this.http.post<AidRequest>(`${this.apiUrl}/${id}/publish`, {});
  }
  updateRequest(id: number, data: Partial<AidRequest>): Observable<AidRequest> {
    return this.http.put<AidRequest>(`${this.apiUrl}/${id}`, data);
  }

  getRequestById(id: number): Observable<AidRequest> {
    return this.http.get<AidRequest>(`${this.apiUrl}/${id}`);
  }

  getUnassignedRequests(): Observable<AidRequest[]> {
    return this.http.get<AidRequest[]>(`${this.apiUrl}/unassigned`).pipe(
      catchError((error) => {
        console.error('Error loading unassigned requests:', error);
        return throwError(() => new Error('Failed to load unassigned requests.'));
      })
    );
  }

  getRequestsBySoldier(soldierId: number): Observable<AidRequest[]> {
    return this.http.get<AidRequest[]>(`${this.apiUrl}/by-soldier/${soldierId}`).pipe(
      catchError((error) => {
        console.error(`Error loading requests for soldier ${soldierId}:`, error);
        return throwError(() => new Error('Failed to load soldier’s requests.'));
      })
    );
  }

  getCompletedRequests(): Observable<AidRequest[]> {
    return this.http.get<AidRequest[]>(`${this.apiUrl}/completed`).pipe(
      catchError((error) => {
        console.error('Error loading completed requests:', error);
        return throwError(() => new Error('Failed to load completed requests.'));
      })
    );
  }
}
