import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SoldierProfileEditComponent } from './soldier-profile-edit.component';

describe('SoldierProfileEditComponent', () => {
  let component: SoldierProfileEditComponent;
  let fixture: ComponentFixture<SoldierProfileEditComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SoldierProfileEditComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SoldierProfileEditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
