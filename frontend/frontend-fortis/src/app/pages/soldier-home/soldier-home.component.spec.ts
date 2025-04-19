import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SoldierHomeComponent } from './soldier-home.component';

describe('SoldierHomeComponent', () => {
  let component: SoldierHomeComponent;
  let fixture: ComponentFixture<SoldierHomeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SoldierHomeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SoldierHomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
