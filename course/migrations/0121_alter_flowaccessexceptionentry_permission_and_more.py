# Generated by Django 5.1 on 2024-09-11 20:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0120_examticket_drop_code_uniqueness"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flowaccessexceptionentry",
            name="permission",
            field=models.CharField(
                choices=[
                    ("view", "View the flow"),
                    ("submit_answer", "Submit answers"),
                    ("end_session", "End session"),
                    ("change_answer", "Change already-graded answer"),
                    ("see_correctness", "See whether an answer is correct"),
                    (
                        "see_answer_before_submission",
                        "See the correct answer before answering",
                    ),
                    (
                        "see_answer_after_submission",
                        "See the correct answer after answering",
                    ),
                    ("cannot_see_flow_result", "Cannot see flow result"),
                    (
                        "set_roll_over_expiration_mode",
                        "Set the session to 'roll over' expiration mode",
                    ),
                    ("see_session_time", "See session time"),
                    ("lock_down_as_exam_session", "Lock down as exam session"),
                    (
                        "send_email_about_flow_page",
                        "Send emails about the flow page to course staff",
                    ),
                    ("hide_point_count", "Hide point count"),
                ],
                max_length=50,
                verbose_name="Permission",
            ),
        ),
        migrations.AlterField(
            model_name="participationpermission",
            name="permission",
            field=models.CharField(
                choices=[
                    ("edit_course", "Edit course"),
                    ("use_admin_interface", "Use admin interface"),
                    ("manage_authentication_tokens", "Manage authentication tokens"),
                    ("impersonate_role", "Impersonate role"),
                    ("set_fake_time", "Set fake time"),
                    ("set_pretend_facility", "Pretend to be in facility"),
                    ("edit_course_permissions", "Edit course permissions"),
                    ("view_hidden_course_page", "View hidden course page"),
                    ("view_calendar", "View calendar"),
                    ("send_instant_message", "Send instant message"),
                    ("access_files_for", "Access files for"),
                    ("included_in_grade_statistics", "Included in grade statistics"),
                    ("skip_during_manual_grading", "Skip during manual grading"),
                    ("edit_exam", "Edit exam"),
                    ("issue_exam_ticket", "Issue exam ticket"),
                    ("batch_issue_exam_ticket", "Batch issue exam ticket"),
                    (
                        "view_participant_masked_profile",
                        "View participants' masked profile only",
                    ),
                    ("view_flow_sessions_from_role", "View flow sessions from role"),
                    ("view_gradebook", "View gradebook"),
                    ("edit_grading_opportunity", "Edit grading opportunity"),
                    ("assign_grade", "Assign grade"),
                    ("view_grader_stats", "View grader stats"),
                    ("batch_import_grade", "Batch-import grades"),
                    ("batch_export_grade", "Batch-export grades"),
                    ("batch_download_submission", "Batch-download submissions"),
                    ("impose_flow_session_deadline", "Impose flow session deadline"),
                    (
                        "batch_impose_flow_session_deadline",
                        "Batch-impose flow session deadline",
                    ),
                    ("end_flow_session", "End flow session"),
                    ("batch_end_flow_session", "Batch-end flow sessions"),
                    ("regrade_flow_session", "Regrade flow session"),
                    ("batch_regrade_flow_session", "Batch-regrade flow sessions"),
                    (
                        "recalculate_flow_session_grade",
                        "Recalculate flow session grade",
                    ),
                    (
                        "batch_recalculate_flow_session_grade",
                        "Batch-recalculate flow session grades",
                    ),
                    ("reopen_flow_session", "Reopen flow session"),
                    ("grant_exception", "Grant exception"),
                    ("view_analytics", "View analytics"),
                    ("preview_content", "Preview content"),
                    ("update_content", "Update content"),
                    ("use_git_endpoint", "Use direct git endpoint"),
                    ("use_markup_sandbox", "Use markup sandbox"),
                    ("use_page_sandbox", "Use page sandbox"),
                    ("test_flow", "Test flow"),
                    ("edit_events", "Edit events"),
                    ("query_participation", "Query participation"),
                    ("edit_participation", "Edit participation"),
                    ("preapprove_participation", "Preapprove participation"),
                    ("manage_instant_flow_requests", "Manage instant flow requests"),
                ],
                db_index=True,
                max_length=200,
                verbose_name="Permission",
            ),
        ),
        migrations.AlterField(
            model_name="participationpreapproval",
            name="roles",
            field=models.ManyToManyField(
                blank=True,
                related_name="+",
                to="course.participationrole",
                verbose_name="Roles",
            ),
        ),
        migrations.AlterField(
            model_name="participationrolepermission",
            name="permission",
            field=models.CharField(
                choices=[
                    ("edit_course", "Edit course"),
                    ("use_admin_interface", "Use admin interface"),
                    ("manage_authentication_tokens", "Manage authentication tokens"),
                    ("impersonate_role", "Impersonate role"),
                    ("set_fake_time", "Set fake time"),
                    ("set_pretend_facility", "Pretend to be in facility"),
                    ("edit_course_permissions", "Edit course permissions"),
                    ("view_hidden_course_page", "View hidden course page"),
                    ("view_calendar", "View calendar"),
                    ("send_instant_message", "Send instant message"),
                    ("access_files_for", "Access files for"),
                    ("included_in_grade_statistics", "Included in grade statistics"),
                    ("skip_during_manual_grading", "Skip during manual grading"),
                    ("edit_exam", "Edit exam"),
                    ("issue_exam_ticket", "Issue exam ticket"),
                    ("batch_issue_exam_ticket", "Batch issue exam ticket"),
                    (
                        "view_participant_masked_profile",
                        "View participants' masked profile only",
                    ),
                    ("view_flow_sessions_from_role", "View flow sessions from role"),
                    ("view_gradebook", "View gradebook"),
                    ("edit_grading_opportunity", "Edit grading opportunity"),
                    ("assign_grade", "Assign grade"),
                    ("view_grader_stats", "View grader stats"),
                    ("batch_import_grade", "Batch-import grades"),
                    ("batch_export_grade", "Batch-export grades"),
                    ("batch_download_submission", "Batch-download submissions"),
                    ("impose_flow_session_deadline", "Impose flow session deadline"),
                    (
                        "batch_impose_flow_session_deadline",
                        "Batch-impose flow session deadline",
                    ),
                    ("end_flow_session", "End flow session"),
                    ("batch_end_flow_session", "Batch-end flow sessions"),
                    ("regrade_flow_session", "Regrade flow session"),
                    ("batch_regrade_flow_session", "Batch-regrade flow sessions"),
                    (
                        "recalculate_flow_session_grade",
                        "Recalculate flow session grade",
                    ),
                    (
                        "batch_recalculate_flow_session_grade",
                        "Batch-recalculate flow session grades",
                    ),
                    ("reopen_flow_session", "Reopen flow session"),
                    ("grant_exception", "Grant exception"),
                    ("view_analytics", "View analytics"),
                    ("preview_content", "Preview content"),
                    ("update_content", "Update content"),
                    ("use_git_endpoint", "Use direct git endpoint"),
                    ("use_markup_sandbox", "Use markup sandbox"),
                    ("use_page_sandbox", "Use page sandbox"),
                    ("test_flow", "Test flow"),
                    ("edit_events", "Edit events"),
                    ("query_participation", "Query participation"),
                    ("edit_participation", "Edit participation"),
                    ("preapprove_participation", "Preapprove participation"),
                    ("manage_instant_flow_requests", "Manage instant flow requests"),
                ],
                db_index=True,
                max_length=200,
                verbose_name="Permission",
            ),
        ),
    ]