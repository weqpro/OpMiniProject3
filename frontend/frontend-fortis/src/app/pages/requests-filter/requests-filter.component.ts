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

  searchTerm = '';
  selectedCategory = '';
  sortOption = '';
  userRole: UserRole | null = null;

  categories = [
    'Автозапчастини',
    'Енергозабезпечення',
    'Гігієна та санітарія',
    'Інструменти / будматеріали',
    'Медикаменти',
    'Навігація',
    'Одяг',
    'Побутові послуги',
    'Польовий побут',
    'Продукти харчування',
    'Ремонт',
    'Розвідка та спостереження',
    'Спорядження',
    'Техніка',
    'Транспорт',
    'Зв\'язок'
  ];

  sortOptions = ['За датою опублікування', 'За терміновістю', 'За релевантністю'];

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
      next: data => this.requests = data,
      error: err => console.error('Error of loading requests', err)
    });
  }

  onCategoryChange(): void {
    this.searchWithFilters();
  }

  onSearch(): void {
    this.searchWithFilters();
  }

  openDetails(id: number | undefined) {
    if (!id) {
      console.error('Invalid ID', id);
      return;
    }
    this.router.navigate(['/requests', id]);
  }
  
  
  private searchWithFilters(): void {
    const options: SearchOptions = {
      text: this.searchTerm,
      category: this.selectedCategory || null,
      tags: [],
      order: this.sortOption
    };

    this.aidRequestService.getFiltered(options).subscribe({
      next: data => this.requests = data,
      error: err => console.error('Помилка фільтрації', err)
    });
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
          alert('Ви погодились допомогти!');
          this.closeRequestPopup();
          this.loadUnassignedRequests();
        },
        error: err => console.error('Помилка при підтвердженні', err)
      });
    },
    error: err => console.error('Помилка автентифікації', err)
  });
}

}
