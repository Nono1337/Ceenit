import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CeenitWatchlistComponent } from './ceenit-watchlist.component';

describe('CeenitWatchlistComponent', () => {
  let component: CeenitWatchlistComponent;
  let fixture: ComponentFixture<CeenitWatchlistComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CeenitWatchlistComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CeenitWatchlistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
