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
  private authUrl = 'api/auth/token';
  private accessToken: string | null = null;
  private isAuthenticatedSubject = new BehaviorSubject<boolean>(false);
  public isAuthenticated$ = this.isAuthenticatedSubject.asObservable();

  constructor(private http: HttpClient) {}

  login(username: string, password: string): Observable<AuthResponse> {
    const body = new URLSearchParams({
      grant_type: 'password',
      username: username,
      password: password,
    });

    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded'
    });

    return this.http.post<AuthResponse>(this.authUrl, body.toString(), { headers }).pipe(
      tap(response => {
        this.accessToken = response.access_token;
        this.isAuthenticatedSubject.next(true);
      }),
      catchError((error: HttpErrorResponse) => throwError(() => new Error(error.message)))
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
    return this.http.get<{ role: UserRole }>('/api/me').pipe(
      map((response: { role: any; }) => response.role)
    );
  }
  getCurrentUser(): Observable<{ id: number, role: UserRole }> {
    return this.http.get<{ id: number, role: UserRole }>('/api/me');
  }
  
}