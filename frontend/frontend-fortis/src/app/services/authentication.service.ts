import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject, Observable, throwError } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';

interface AuthResponse {
  access_token: string;
  expires_in: number;
  token_type: string;
  scope?: string;
}

@Injectable({ providedIn: 'root' })
export class AuthService {
  private authUrl = 'endpoint';
  private accessToken: string | null = null;
  private isAuthenticatedSubject = new BehaviorSubject<boolean>(false);
  public isAuthenticated$ = this.isAuthenticatedSubject.asObservable();

  constructor(private http: HttpClient) {}

  login(username: string, password: string): Observable<AuthResponse> {
    const body = new URLSearchParams({
      grant_type: 'password',
      username: username,
      password: password,
      client_id: '#',
      client_secret: '#'
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
}
