import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MainQuoteComponent } from './main-quote.component';

describe('MainQuoteComponent', () => {
  let component: MainQuoteComponent;
  let fixture: ComponentFixture<MainQuoteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MainQuoteComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MainQuoteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
