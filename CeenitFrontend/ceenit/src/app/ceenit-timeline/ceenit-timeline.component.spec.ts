import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CeenitTimelineComponent } from './ceenit-timeline.component';

describe('CeenitTimelineComponent', () => {
  let component: CeenitTimelineComponent;
  let fixture: ComponentFixture<CeenitTimelineComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CeenitTimelineComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CeenitTimelineComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
