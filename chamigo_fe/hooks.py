app_name = "chamigo_fe"
app_title = "Chamigo FE"
app_publisher = "Luis Ferreira"
app_description = "Integracion de Factura Electronica para Chamigo"
app_email = "luisgallas.com@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "chamigo_fe",
# 		"logo": "/assets/chamigo_fe/logo.png",
# 		"title": "Chamigo FE",
# 		"route": "/chamigo_fe",
# 		"has_permission": "chamigo_fe.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/chamigo_fe/css/chamigo_fe.css"
# app_include_js = "/assets/chamigo_fe/js/chamigo_fe.js"

# include js, css files in header of web template
# web_include_css = "/assets/chamigo_fe/css/chamigo_fe.css"
# web_include_js = "/assets/chamigo_fe/js/chamigo_fe.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "chamigo_fe/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "chamigo_fe/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "chamigo_fe.utils.jinja_methods",
# 	"filters": "chamigo_fe.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "chamigo_fe.install.before_install"
# after_install = "chamigo_fe.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "chamigo_fe.uninstall.before_uninstall"
# after_uninstall = "chamigo_fe.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "chamigo_fe.utils.before_app_install"
# after_app_install = "chamigo_fe.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "chamigo_fe.utils.before_app_uninstall"
# after_app_uninstall = "chamigo_fe.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "chamigo_fe.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "chamigo_fe.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"chamigo_fe.tasks.all"
# 	],
# 	"daily": [
# 		"chamigo_fe.tasks.daily"
# 	],
# 	"hourly": [
# 		"chamigo_fe.tasks.hourly"
# 	],
# 	"weekly": [
# 		"chamigo_fe.tasks.weekly"
# 	],
# 	"monthly": [
# 		"chamigo_fe.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "chamigo_fe.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "chamigo_fe.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "chamigo_fe.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "chamigo_fe.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["chamigo_fe.utils.before_request"]
# after_request = ["chamigo_fe.utils.after_request"]

# Job Events
# ----------
# before_job = ["chamigo_fe.utils.before_job"]
# after_job = ["chamigo_fe.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"chamigo_fe.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []


fixtures = [
    {
        "dt": "DocType",
        "filters": [
            ["name", "in", ["Factura Electronica"]]
        ]
    },
    {
        "dt": "Server Script",
        "filters": [
            ["name", "in", ["Crear Factura Electronica"]]
        ]
    }
]

# Custom Fields para Factura Electronica
fixtures += [
    {
        "dt": "Custom Field",
        "filters": [
            ["dt", "=", "Factura Electronica"],
            ["fieldname", "in", ["cdc", "estado_sifen"]]
        ]
    }
]
