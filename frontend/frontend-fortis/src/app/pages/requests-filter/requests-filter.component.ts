import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import {AidRequest} from '../../schemas/aid-request';
import {AidRequestService} from '../../services/aid-request.service';
import {SearchOptions} from '../../schemas/search-options';



@Component({
  selector: 'app-requests-filter',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './requests-filter.component.html',
  styleUrls: ['./requests-filter.component.css']
})
export class RequestsFilterComponent implements OnInit {
  requests: AidRequest[] = [];

  searchTerm = '';
  selectedCategory = '';
  sortOption = '';

  categories = ['Автозапчастини' +
  'Енергозабезпечення' +
  'Гігієна та санітарія' +
  'Інструменти / будматеріали' +
  'Медикаменти' +
  'Навігація' +
  'Одяг' +
  'Побутові послуги' +
  'Польовий побут' +
  'Продукти харчування' +
  'Ремонт' +
  'Розвідка та спостереження' +
  'Спорядження' +
  'Техніка' +
  'Транспорт ' +
  'Зв\'язок'];
  sortOptions = ['За датою опублікування', 'За терміновістю','За релевантністю'];

  constructor(private aidRequestService: AidRequestService) {}

  ngOnInit(): void {
    this.loadUnassignedRequests();
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
}
