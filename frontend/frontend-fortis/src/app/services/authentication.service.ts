import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import {BehaviorSubject, map, Observable, throwError} from 'rxjs';
import { catchError, tap } from 'rxjs/operators';

interface AuthResponse {
  access_token: string;
  token_type: string;
}

export type UserRole = 'soldier' | 'volunteer';
@Injectable({ providedIn: 'root' })
export class AuthService {
  private authUrl = 'http://77.110.116.47:8000/api/v1/auth/token';
  private accessToken: string | null = null;
  private isAuthenticatedSubject = new BehaviorSubject<boolean>(false);
  public isAuthenticated$ = this.isAuthenticatedSubject.asObservable();

  constructor(private http: HttpClient) {
    if (typeof window !== 'undefined') {
      this.accessToken = localStorage.getItem('access_token');
    }
  }
  

  login(username: string, password: string, role: 'soldier' | 'volunteer'): Observable<AuthResponse> {
    const body = new URLSearchParams({
      username,
      password,
    });
  
    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded',
    });
  
    return this.http.post<AuthResponse>(`${this.authUrl}/${role}`, body.toString(), { headers }).pipe(
      
      tap(response => {
        localStorage.setItem('access_token', response.access_token);
        this.isAuthenticatedSubject.next(true);
      })
    );
  }

  logout(): void {
    this.accessToken = null;
    this.isAuthenticatedSubject.next(false);
  }

  getAccessToken(): string | null {
    return this.accessToken;
  }

  getUserRole(): Observable<UserRole> {
    return this.http.get<{ role: UserRole }>('http://77.110.116.47:8000/api/v1/auth/me').pipe(
      map((response: { role: any; }) => response.role)
    );
  }
  getCurrentUser(): Observable<{ id: number, role: UserRole }> {
    return this.http.get<{ id: number, role: UserRole }>('http://77.110.116.47:8000/api/v1/auth/me');
  }
  
}