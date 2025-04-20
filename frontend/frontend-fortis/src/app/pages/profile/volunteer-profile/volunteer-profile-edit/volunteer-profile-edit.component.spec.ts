import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VolunteerProfileEditComponent } from './volunteer-profile-edit.component';

describe('VolunteerProfileEditComponent', () => {
  let component: VolunteerProfileEditComponent;
  let fixture: ComponentFixture<VolunteerProfileEditComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VolunteerProfileEditComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VolunteerProfileEditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
