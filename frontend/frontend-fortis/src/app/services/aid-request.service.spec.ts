import { TestBed } from '@angular/core/testing';

import { AidRequestService } from './aid-request.service';

describe('AidRequestService', () => {
  let service: AidRequestService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AidRequestService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
