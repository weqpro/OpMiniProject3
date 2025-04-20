import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SoldierProfileComponent } from './soldier-profile.component';

describe('SoldierProfileComponent', () => {
  let component: SoldierProfileComponent;
  let fixture: ComponentFixture<SoldierProfileComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SoldierProfileComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SoldierProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
