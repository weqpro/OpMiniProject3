import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import {AidRequest} from '../../schemas/aid-request';
import {AidRequestService} from '../../services/aid-request.service';


@Component({
  selector: 'app-my-requests',
  standalone: true,
  imports: [CommonModule, MatButtonModule],
  templateUrl: './my-requests.component.html',
  styleUrls: ['./my-requests.component.css']
})
export class MyRequestsComponent implements OnInit {
  requests: AidRequest[] = [];
  userRole: 'soldier' | 'volunteer' = 'soldier';//тут треба зробити

  constructor(private aidRequestService: AidRequestService) {}

  ngOnInit(): void {
    this.loadMyRequests();
  }

  loadMyRequests(): void {
    this.aidRequestService.getAllRequests().subscribe({
      next: data => this.requests = data,
      error: err => console.error('Не вдалося завантажити запити', err)
    });
  }
}
