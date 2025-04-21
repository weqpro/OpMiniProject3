import { Component, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatChipsModule } from '@angular/material/chips';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatMenuModule } from '@angular/material/menu';

@Component({
  selector: 'app-review',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule,
    MatFormFieldModule,
    MatInputModule,
    MatChipsModule,
    MatIconModule,
    MatButtonModule,
    MatMenuModule,
  ],
  templateUrl: './review.component.html',
  styleUrls: ['./review.component.css'],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class ReviewComponent {
  rating = 0;
  tags: string[] = [];

  positiveTags = [
    'швидко',
    'якісно',
    'вчасно',
    'завжди на зв’язку',
    'приємне спілкування',
    'рекомендую'
  ];

  negativeTags = [
    'повільно',
    'неякісно',
    'не вийшов на звʼязок',
    'затримка без попередження',
    'не дотримався умов',
    'неорганізовано',
  ];

  selectedTags: string[] = [];

  setRating(star: number): void {
    this.rating = star;
    if (star >= 4) {
      this.tags = [...this.positiveTags];
    } else if (star > 0) {
      this.tags = [...this.negativeTags];
    } else {
      this.tags = [];
    }
    this.selectedTags = [];
  }

  toggleTag(tag: string): void {
    const index = this.selectedTags.indexOf(tag);
    if (index >= 0) {
      this.selectedTags.splice(index, 1);
    } else {
      this.selectedTags.push(tag);
    }
  }
}
