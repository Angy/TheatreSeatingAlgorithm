from django.contrib import admin

from app.models import Row, Seat, Hall, User, Section


class SectionInlineAdmin(admin.TabularInline):
    model = Section.rows.through
    extra = 0
    verbose_name = 'Section'
    verbose_name_plural = 'Sections'


class RowInLineAdmin(admin.TabularInline):
    model = Row.seats.through
    extra = 0
    verbose_name = 'Row'
    verbose_name_plural = 'Rows'


@admin.register(Row)
class RowAdmin(admin.ModelAdmin):
    model = Row
    fields = ('row_number', 'seats')
    filter_horizontal = ('seats', )
    inlines = (SectionInlineAdmin, )

    # display seats that are not blocked yet
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "seats":
            kwargs["queryset"] = Seat.objects.filter(is_blocked=False)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    model = Seat
    fields = ('seat_type', 'seat_number', 'allocated_to',)
    inlines = (RowInLineAdmin, )


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    model = Hall
    fields = ('name', 'sections', )
    list_display = ('name', )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ('user_name', 'rank', )
    list_display = ('user_name', 'rank', )
    list_filter = ('rank', )


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    model = Section
    fields = ('section_name', 'rows', )
    filter_horizontal = ('rows', )
