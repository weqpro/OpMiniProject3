import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VolunteerChangePasswordComponent } from './volunteer-change-password.component';

describe('VolunteerChangePasswordComponent', () => {
  let component: VolunteerChangePasswordComponent;
  let fixture: ComponentFixture<VolunteerChangePasswordComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VolunteerChangePasswordComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VolunteerChangePasswordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
