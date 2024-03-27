from Infra.api_wrapper import APIWrapper
from Utils.read_from_env import Credentials
import requests
import asana
from asana.rest import ApiException

from pprint import pprint


class AsanaApiRequests:

    url = 'https://app.asana.com/api/1.0/projects/1206935539102605'

    def __init__(self, api_object):
        self.data = Credentials()
        self.token = self.data.get_token()
        self.ApiKey = self.data.get_apikey()
        self.my_api = APIWrapper()
        self.headers = {
            "Accept": "application/json",
            "Authorization": self.ApiKey}
        configuration = asana.Configuration()
        configuration.access_token = self.token
        self.api_client = asana.ApiClient(configuration)


   # def get_a_project_asana_website(self):
    #    result = requests.get(self.url, headers=self.headers)
   #     response_body_json = result.json()
   #     project_name = response_body_json["data"][0]["name"]
   #     print(project_name)
   #     return result

    def get_asana_task_name_by_api(self):
        projects_api_instance = asana.ProjectsApi(self.api_client)
        project_gid = '1206935539102605'
        tasks = self.api_client.tasks.find_by_project(project_gid)
        opts = {
            'opt_fields': "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,project_brief,public,start_on,team,team.name,workspace,workspace.name",
            # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        }

        try:
            # Get a project
            api_response = projects_api_instance.get_project(project_gid, opts)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ProjectsApi->get_project: %s\n" % e)
        print(tasks['name'])



