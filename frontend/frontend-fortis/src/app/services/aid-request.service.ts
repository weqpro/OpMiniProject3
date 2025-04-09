import {inject, Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable, throwError} from 'rxjs';
import {SearchOptions} from '../schemas/search-options';
import {AidRequest} from '../schemas/aid-request';

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
}
