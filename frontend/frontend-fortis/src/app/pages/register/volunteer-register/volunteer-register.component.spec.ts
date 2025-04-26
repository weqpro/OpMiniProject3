import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VolunteerRegisterComponent } from './volunteer-register.component';

describe('VolunteerRegisterComponent', () => {
  let component: VolunteerRegisterComponent;
  let fixture: ComponentFixture<VolunteerRegisterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VolunteerRegisterComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VolunteerRegisterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
