import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatSelectModule } from '@angular/material/select';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
import { MatExpansionModule } from '@angular/material/expansion';
import { AidRequestService } from '../../services/aid-request.service';
import { AuthService } from '../../services/authentication.service';
import { MatMenuModule } from '@angular/material/menu';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-create-post',
  standalone: true,
  providers: [AidRequestService],
  templateUrl: './create-post.component.html',
  styleUrls: ['./create-post.component.css'],
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
  ]
})
export class CreatePostComponent implements OnInit {
  name = '';
  description = '';
  image: string = '';
  location = '';
  endDate: Date | null = null;
  status = 'Опубліковано';
  soldier_id!: number;
  category_id: number | null = null;

  selectedFile: File | null = null;
  imagePreview: string | null = null;
  imageSelected: boolean = false;

  categories = [
    { id: 1, name: 'Автозапчастини' },
    { id: 2, name: 'Енергозабезпечення' },
    { id: 3, name: 'Генератори' },
    { id: 4, name: 'Гігієна та санітарія' },
    { id: 5, name: 'Інструменти / будматеріали' },
    { id: 6, name: 'Медицина' },
    { id: 7, name: 'Навігація' },
    { id: 8, name: 'Одяг' },
    { id: 9, name: 'Побутові послуги' },
    { id: 10, name: 'Польовий побут' },
    { id: 11, name: 'Продукти харчування' },
    { id: 12, name: 'Ремонт' },
    { id: 13, name: 'Розвідка і спостереження' },
    { id: 14, name: 'Спорядження' },
    { id: 15, name: 'Техніка' },
    { id: 16, name: 'Транспорт' },
    { id: 17, name: 'Звʼязок' }
  ];

  
  cities: string[] = [
    "Івано-Франківськ",
    "Ізмаїл",
    "Ізюм",
    "Ірпінь",
    "Іршава",
    "Авдіївка",
    "Балаклія",
    "Бар",
    "Бахмут",
    "Баштанка",
    "Бердичів",
    "Бердянськ",
    "Бережани",
    "Богодухів",
    "Бориспіль",
    "Борщів",
    "Броди",
    "Бровари",
    "Буча",
    "Біла Церква",
    "Білгород-Дністровський",
    "Боярка",
    "Володимир-Волинський",
    "Вовчанськ",
    "Волноваха",
    "Василівка",
    "Вознесенськ",
    "Вугледар",
    "Гайсин",
    "Гола Пристань",
    "Горлівка",
    "Дергачі",
    "Дніпро",
    "Донецьк",
    "Дрогобич",
    "Дружківка",
    "Дубно",
    "Енергодар",
    "Житомир",
    "Запоріжжя",
    "Звенигородка",
    "Золоте",
    "Івано-Франківськ", 
    "Кам'янець-Подільський",
    "Кам'янське",
    "Київ",
    "Ковель",
    "Конотоп",
    "Костянтинівка",
    "Краматорськ",
    "Кременчук",
    "Кремінна",
    "Кривий Ріг",
    "Кропивницький",
    "Куп’янськ",
    "Ладижин",
    "Лиман",
    "Лисичанськ",
    "Луцьк",
    "Львів",
    "Лозова",
    "Лубни",
    "Малин",
    "Мар’їнка",
    "Маріуполь",
    "Мелітополь",
    "Миргород",
    "Мирноград",
    "Миколаїв",
    "Мукачево",
    "Ніжин",
    "Нікополь",
    "Нова Каховка",
    "Новоград-Волинський",
    "Новодністровськ",
    "Новомиргород",
    "Новоайдар",
    "Одеса",
    "Овруч",
    "Очаків",
    "Первомайськ",
    "Полтава",
    "Покров",
    "Покровськ",
    "Попасна",
    "Прилуки",
    "Рівне",
    "Ромни",
    "Рубіжне",
    "Сарни",
    "Святогірськ",
    "Світлодарськ",
    "Сіверодарськ?",
    "Сєвєродонецьк",
    "Синельникове",
    "Сміла",
    "Слов’янськ",
    "Сокаль",
    "Соледар",
    "Старокостянтинів",
    "Стрий",
    "Суми",
    "Токмак",
    "Торецьк",
    "Тернопіль",
    "Ужгород",
    "Умань",
    "Фастів",
    "Харків",
    "Херсон",
    "Хмельницький",
    "Хуст",
    "Часів Яр",
    "Черкаси",
    "Чернівці",
    "Чернігів",
    "Чорноморськ",
    "Чугуїв",
    "Шепетівка",
    "Щастя",
    "Южне",
    "Яготин",
  ];
  

  constructor(
    private router: Router,
    private aidRequestService: AidRequestService,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    this.authService.getCurrentUser().subscribe({
      next: user => {
        this.soldier_id = user.id;
      },
      error: err => {
        console.error('Не вдалося отримати користувача', err);
      },
    });
  }

  triggerImageInput(): void {
    document.getElementById('imageInput')?.click();
  }

  onImageSelected(event: Event): void {
    const file = (event.target as HTMLInputElement).files?.[0];
    if (file) {
      this.selectedFile = file;
      this.image = file.name;
      this.imageSelected = true;

      const reader = new FileReader();
      reader.onload = () => {
        this.imagePreview = reader.result as string;
      };
      reader.readAsDataURL(file);
    }
  }

  openDetails(requestId: number): void {
    this.router.navigate(['/request', requestId]);
  }

  publishRequest(): void {
    if (!this.category_id) {
      Swal.fire({
        icon: 'warning',
        title: 'Увага',
        text: 'Оберіть категорію!',
        confirmButtonColor: '#39736b',
        confirmButtonText: 'Гаразд',
        customClass: {
          confirmButton: 'montserrat-button'
        }
      });
      return;
    }

    const payload = {
      name: this.name,
      description: this.description,
      location: this.location,
      deadline: this.endDate || new Date(),
      category_id: this.category_id
    };

    const formData = new FormData();
    formData.append('json_data', JSON.stringify(payload));

    if (this.selectedFile) {
      formData.append('image', this.selectedFile);
    }

    this.aidRequestService.createRequest(formData).subscribe({
      next: () => {
        Swal.fire({
          icon: 'success',
          title: 'Запит створено!',
          text: 'Дякуємо!',
          confirmButtonColor: '#39736b',
          confirmButtonText: 'Гаразд',
          customClass: {
            confirmButton: 'montserrat-button'
          }
        }).then(() => this.router.navigate(['/profile/soldier']));
      },
      error: (err) => {
        console.error(err);
        Swal.fire({
          icon: 'error',
          title: 'Помилка',
          text: 'Не вдалося створити запит.',
          confirmButtonColor: '#39736b',
          confirmButtonText: 'Гаразд',
          customClass: {
            confirmButton: 'montserrat-button'
          }
        });
      }
    });
  }

  logout(): void {
    this.authService.logout();
    this.router.navigate(['/login']);
  }
}
