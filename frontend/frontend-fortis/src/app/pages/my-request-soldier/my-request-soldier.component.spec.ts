import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MyRequestSoldierComponent } from './my-request-soldier.component';

describe('MyRequestSoldierComponent', () => {
  let component: MyRequestSoldierComponent;
  let fixture: ComponentFixture<MyRequestSoldierComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MyRequestSoldierComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MyRequestSoldierComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
