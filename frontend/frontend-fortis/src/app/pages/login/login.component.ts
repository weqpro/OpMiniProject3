import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  imports: [
    FormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatIconModule,
  ]
})
export class LoginComponent {
  email: string = '';
  password: string = '';
  selectedRole: 'volunteer' | 'soldier' = 'volunteer';
  baseUrl: string = 'http://127.0.0.1:8000/api/v1/auth/token';

  constructor(private http: HttpClient, private router: Router) {}

  selectRole(role: 'volunteer' | 'soldier') {
    this.selectedRole = role;
  }

  login() {
    const endpoint = `${this.baseUrl}/${this.selectedRole}`;
    const body = new URLSearchParams();
      body.set('username', this.email);
      body.set('password', this.password);

      const headers = { 'Content-Type': 'application/x-www-form-urlencoded' };

      this.http.post(endpoint, body.toString(), { headers }).subscribe({
        next: (response: any) => {
          localStorage.setItem('access_token', response.access_token);
          this.router.navigate(['/requests-filter']);
        },
        error: () => {
          alert('Неправильна електронна адреса або пароль.\nНе маєте акаунту? Зареєструйтесь!');
        }
      });

  }

  goToRegister() {
    this.router.navigate(['/role-selection']);
  }
}