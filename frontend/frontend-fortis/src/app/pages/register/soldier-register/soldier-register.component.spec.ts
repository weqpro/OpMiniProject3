import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SoldierRegisterComponent } from './soldier-register.component';

describe('SoldierRegisterComponent', () => {
  let component: SoldierRegisterComponent;
  let fixture: ComponentFixture<SoldierRegisterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SoldierRegisterComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SoldierRegisterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
