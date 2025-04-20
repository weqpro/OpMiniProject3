import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {SoldierService} from '../../../../services/soldier.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-soldier-profile-edit',
  imports: [],
  templateUrl: './soldier-profile-edit.component.html',
  standalone: true,
  styleUrl: './soldier-profile-edit.component.css'
})
export class SoldierProfileEditComponent implements OnInit {
  form!: FormGroup;

  constructor(private fb: FormBuilder, private soldierService: SoldierService, private router: Router) {}

  ngOnInit(): void {
    this.form = this.fb.group({
      name: ['', Validators.required],
      surname: ['', Validators.required],
      phone_number: [''],
      email: ['', [Validators.required, Validators.email]],
      unit: [''],
      subsubunit: [''],
      battalion: ['']
    });

    this.soldierService.getProfile().subscribe(profile => {
      this.form.patchValue(profile);
    });
  }

  submit() {
    if (this.form.valid) {
      this.soldierService.updateProfile(this.form.value).subscribe({
        next: () => this.router.navigate(['/profile/soldier']),
        error: err => alert('Не вдалося оновити')
      });
    }
  }
}

