import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Review } from '../schemas/review';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ReviewService {
  private apiUrl = 'http://127.0.0.1:8000/api/v1/reviews';

  constructor(private http: HttpClient) {}

  getReviewsByVolunteer(volunteerId: number): Observable<Review[]> {
    return this.http.get<Review[]>(`${this.apiUrl}/by-volunteer/${volunteerId}`);
  }
}