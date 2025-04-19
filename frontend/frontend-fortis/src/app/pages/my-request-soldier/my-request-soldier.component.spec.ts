import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MyRequestsComponent } from './my-request-soldier.component';

describe('MyRequestSoldierComponent', () => {
  let component: MyRequestsComponent;
  let fixture: ComponentFixture<MyRequestsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MyRequestsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MyRequestsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});