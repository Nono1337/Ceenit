import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CeenitReviewsComponent } from './ceenit-reviews.component';

describe('CeenitReviewsComponent', () => {
  let component: CeenitReviewsComponent;
  let fixture: ComponentFixture<CeenitReviewsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CeenitReviewsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CeenitReviewsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
