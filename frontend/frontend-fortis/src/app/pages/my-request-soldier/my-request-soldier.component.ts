import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import {AidRequest} from '../../schemas/aid-request';
import {AidRequestService} from '../../services/aid-request.service';
import {AuthService, UserRole} from '../../services/authentication.service';


@Component({
  selector: 'app-my-requests',
  standalone: true,
  imports: [CommonModule, MatButtonModule],
  templateUrl: './my-requests.component.html',
  styleUrls: ['./my-requests.component.css']
})
export class MyRequestsComponent implements OnInit {
  requests: AidRequest[] = [];
  userRole: UserRole | null = null;

  constructor(private aidRequestService: AidRequestService, private authService: AuthService) {}

  ngOnInit(): void {
    this.authService.getUserRole().subscribe({
      next: role => {
        this.userRole = role;
        this.loadMyRequests();
      },
      error: err => {
        console.error('Не вдалося отримати роль користувача', err);
      }
    });
  }

  loadMyRequests(): void {
    this.aidRequestService.getAllRequests().subscribe({
      next: data => this.requests = data,
      error: err => console.error('Не вдалося завантажити запити', err)
    });
  }
}
