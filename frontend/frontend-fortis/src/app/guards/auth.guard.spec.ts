import { TestBed } from '@angular/core/testing';
import { AuthGuard } from './auth.guard';
import { Router } from '@angular/router';
import { AuthService } from '../services/authentication.service';

describe('AuthGuard', () => {
  let guard: AuthGuard;
  let routerSpy = jasmine.createSpyObj('Router', ['navigate']);
  let authServiceSpy = jasmine.createSpyObj('AuthService', ['getAccessToken']);

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        AuthGuard,
        { provide: Router, useValue: routerSpy },
        { provide: AuthService, useValue: authServiceSpy }
      ]
    });

    guard = TestBed.inject(AuthGuard);
  });

  it('should allow if token exists', () => {
    localStorage.setItem('access_token', 'test');
    expect(guard.canActivate()).toBeTrue();
  });

  it('should block and redirect if no token', () => {
    localStorage.removeItem('access_token');
    expect(guard.canActivate()).toBeFalse();
    expect(routerSpy.navigate).toHaveBeenCalledWith(['/']);
  });
});
