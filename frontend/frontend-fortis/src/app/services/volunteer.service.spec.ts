import { TestBed } from '@angular/core/testing';

import { VolonteerService } from './volunteer.service';

describe('VolonteerService', () => {
  let service: VolonteerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(VolonteerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
