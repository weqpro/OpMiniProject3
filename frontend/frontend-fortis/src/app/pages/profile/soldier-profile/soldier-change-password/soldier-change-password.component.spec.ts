import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SoldierChangePasswordComponent } from './soldier-change-password.component';

describe('SoldierChangePasswordComponent', () => {
  let component: SoldierChangePasswordComponent;
  let fixture: ComponentFixture<SoldierChangePasswordComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SoldierChangePasswordComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SoldierChangePasswordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
