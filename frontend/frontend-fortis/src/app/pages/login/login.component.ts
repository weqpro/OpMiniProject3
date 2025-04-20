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
  baseUrl: string = 'http://localhost:8000/api/v1/token';

  constructor(private http: HttpClient, private router: Router) {}

  selectRole(role: 'volunteer' | 'soldier') {
    this.selectedRole = role;
  }

  login() {
    const endpoint = `${this.baseUrl}/${this.selectedRole}`;
    const body = {
      username: this.email,
      password: this.password
    };

    this.http.post(endpoint, body).subscribe({
      next: (response: any) => {
        localStorage.setItem('access_token', response.access_token);
        this.router.navigate(['/requests-filter']);
      },
      error: () => {
        alert('Невірний email або пароль');
      }
    });
  }

  goToRegister() {
    this.router.navigate(['/role-selection']);
  }
}
