import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AidRequest } from '../../schemas/aid-request';
import { AidRequestService } from '../../services/aid-request.service';
import { SearchOptions } from '../../schemas/search-options';
import { RouterModule } from '@angular/router';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatSelectModule } from '@angular/material/select';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatMenuModule } from '@angular/material/menu';
import { AuthService, UserRole } from '../../services/authentication.service';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-requests-filter',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    RouterModule,
    MatFormFieldModule,
    MatSelectModule,
    MatDatepickerModule,
    MatNativeDateModule,
    MatInputModule,
    MatExpansionModule,
    MatIconModule,
    MatButtonModule,
    MatMenuModule
  ],
  templateUrl: './requests-filter.component.html',
  styleUrls: ['./requests-filter.component.css']
})
export class RequestsFilterComponent implements OnInit {
  requests: AidRequest[] = [];
  allRequests: AidRequest[] = [];

  searchTerm = '';
  searchCity = '';
  selectedCategoryId: number | null = null;
  sortOption = '';
  userRole: UserRole | null = null;

  categories = [
    { id: 1, name: 'Автозапчастини' },
    { id: 2, name: 'Енергозабезпечення' },
    { id: 3, name: 'Гігієна та санітарія' },
    { id: 4, name: 'Інструменти / будматеріали' },
    { id: 5, name: 'Медикаменти' },
    { id: 6, name: 'Навігація' },
    { id: 7, name: 'Одяг' },
    { id: 8, name: 'Побутові послуги' },
    { id: 9, name: 'Польовий побут' },
    { id: 10, name: 'Продукти харчування' },
    { id: 11, name: 'Ремонт' },
    { id: 12, name: 'Розвідка та спостереження' },
    { id: 13, name: 'Спорядження' },
    { id: 14, name: 'Техніка' },
    { id: 15, name: 'Транспорт' },
    { id: 16, name: 'Зв\'язок' }
  ];

  constructor(
    private aidRequestService: AidRequestService,
    private authService: AuthService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.loadUnassignedRequests();

    this.authService.getCurrentUser().subscribe({
      next: user => {
        this.userRole = user.role;
      },
      error: err => console.error('Не вдалося отримати користувача', err)
    });
  }

  loadUnassignedRequests(): void {
    this.aidRequestService.getUnassignedRequests().subscribe({
      next: data => {
        this.allRequests = data;
        this.requests = [...this.allRequests];
      },
      error: err => console.error('Error of loading requests', err)
    });
  }

  onCategoryChange(): void {
    if (!this.selectedCategoryId) {
      this.requests = [...this.allRequests];
    } else {
      this.requests = this.allRequests.filter(r => r.category_id === this.selectedCategoryId);
    }
  }

  onSearch(): void {
    const searchTermLower = this.searchTerm.toLowerCase();
    this.requests = this.allRequests.filter(r => r.name.toLowerCase().includes(searchTermLower));
  }

  onCitySearch(): void {
    if (!this.searchCity.trim()) {
      this.loadUnassignedRequests();
      return;
    }

    this.aidRequestService.getRequestsByCity(this.searchCity).subscribe({
      next: data => this.requests = data,
      error: err => console.error('Помилка пошуку за містом', err)
    });
  }

  openDetails(id: number | undefined) {
    if (!id) {
      console.error('Invalid ID', id);
      return;
    }
    this.router.navigate(['/requests', id]);
  }

  selectedRequest: any = null;

  openRequestPopup(request: any): void {
    this.selectedRequest = request;
  }

  closeRequestPopup(): void {
    this.selectedRequest = null;
  }

  acceptRequest(): void {
    if (!this.selectedRequest?.id) {
      console.error('ID запиту не знайдено');
      return;
    }

    this.authService.getCurrentUser().subscribe({
      next: user => {
        const volunteerId = user.id;
        this.aidRequestService.assignToVolunteer(this.selectedRequest.id, volunteerId).subscribe({
          next: () => {
            Swal.fire({
              icon: 'success',
              title: 'Успішно!',
              text: 'Ви погодились допомогти!',
              confirmButtonColor: '#39736b',
              confirmButtonText: 'Окей'
            });
            this.closeRequestPopup();
            this.loadUnassignedRequests();
          },
          error: err => {
            console.error('Помилка при підтвердженні', err);
            Swal.fire({
              icon: 'error',
              title: 'Помилка',
              text: 'Не вдалося погодитись допомогти. Спробуйте ще раз.',
              confirmButtonColor: '#39736b',
              confirmButtonText: 'Окей'
            });
          }
        });
      },
      error: err => console.error('Помилка автентифікації', err)
    });
  }
}
 