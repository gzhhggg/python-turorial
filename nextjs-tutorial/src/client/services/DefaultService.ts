/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ClientPydantic } from '../models/ClientPydantic';
import type { ClientPydanticCreate } from '../models/ClientPydanticCreate';
import type { MemberCost } from '../models/MemberCost';
import type { MemberCostCreate } from '../models/MemberCostCreate';
import type { MemberCostCreateResponse } from '../models/MemberCostCreateResponse';
import type { MemberPydantic } from '../models/MemberPydantic';
import type { MemberPydanticCreate } from '../models/MemberPydanticCreate';
import type { Project } from '../models/Project';
import type { ProjectBudget } from '../models/ProjectBudget';
import type { ProjectBudgetCreate } from '../models/ProjectBudgetCreate';
import type { ProjectBudgetCreateResponse } from '../models/ProjectBudgetCreateResponse';
import type { ProjectCreate } from '../models/ProjectCreate';
import type { ProjectCreateResponse } from '../models/ProjectCreateResponse';
import type { ProjectMemberAssign } from '../models/ProjectMemberAssign';
import type { ProjectMemberAssignCreate } from '../models/ProjectMemberAssignCreate';
import type { ProjectMemberAssignCreateResponse } from '../models/ProjectMemberAssignCreateResponse';
import type { ProjectSlot } from '../models/ProjectSlot';
import type { ProjectSlotCreate } from '../models/ProjectSlotCreate';
import type { ProjectSlotCreateResponse } from '../models/ProjectSlotCreateResponse';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class DefaultService {
    /**
     * Get Clients
     * @returns ClientPydantic Successful Response
     * @throws ApiError
     */
    public static getClientsClientsGet({
        sort = '["id","ASC"]',
        range = '[0,9]',
        filter = '{}',
    }: {
        sort?: string,
        range?: string,
        filter?: string,
    }): CancelablePromise<Array<ClientPydantic>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/clients',
            query: {
                'sort': sort,
                'range': range,
                'filter': filter,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Create Client
     * @returns ClientPydantic Successful Response
     * @throws ApiError
     */
    public static createClientClientsPost({
        requestBody,
    }: {
        requestBody: ClientPydanticCreate,
    }): CancelablePromise<ClientPydantic> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/clients',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Many Client
     * @returns void
     * @throws ApiError
     */
    public static deleteManyClientClientsDelete({
        filter = '{}',
    }: {
        filter?: string,
    }): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/clients',
            query: {
                'filter': filter,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Client
     * @returns ClientPydantic Successful Response
     * @throws ApiError
     */
    public static getClientClientsClientIdGet({
        clientId,
    }: {
        clientId: number,
    }): CancelablePromise<ClientPydantic> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/clients/{client_id}',
            path: {
                'client_id': clientId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Client
     * @returns ClientPydantic Successful Response
     * @throws ApiError
     */
    public static updateClientClientsClientIdPut({
        requestBody,
    }: {
        requestBody: ClientPydantic,
    }): CancelablePromise<ClientPydantic> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/clients/{client_id}',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Client
     * @returns void
     * @throws ApiError
     */
    public static deleteClientClientsClientIdDelete({
        clientId,
    }: {
        clientId: number,
    }): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/clients/{client_id}',
            path: {
                'client_id': clientId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Projects
     * @returns Project Successful Response
     * @throws ApiError
     */
    public static getProjectsProjectsGet(): CancelablePromise<Array<Project>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/projects',
        });
    }
    /**
     * Create Project
     * @returns ProjectCreateResponse Successful Response
     * @throws ApiError
     */
    public static createProjectProjectsPost({
        requestBody,
    }: {
        requestBody: ProjectCreate,
    }): CancelablePromise<ProjectCreateResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/projects',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Projects
     * @returns Project Successful Response
     * @throws ApiError
     */
    public static updateProjectsProjectsProjectsIdPut({
        projectsId,
        requestBody,
    }: {
        projectsId: number,
        requestBody: ProjectCreate,
    }): CancelablePromise<Project> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/projects/{projects_id}',
            path: {
                'projects_id': projectsId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Projects
     * @returns void
     * @throws ApiError
     */
    public static deleteProjectsProjectsProjectsIdDelete({
        projectsId,
    }: {
        projectsId: number,
    }): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/projects/{projects_id}',
            path: {
                'projects_id': projectsId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Members
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getMembersMembersGet({
        sort = '["id","ASC"]',
        range = '[0,9]',
        filter = '{}',
    }: {
        sort?: string,
        range?: string,
        filter?: string,
    }): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/members',
            query: {
                'sort': sort,
                'range': range,
                'filter': filter,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Create Member
     * @returns MemberPydantic Successful Response
     * @throws ApiError
     */
    public static createMemberMembersPost({
        requestBody,
    }: {
        requestBody: MemberPydanticCreate,
    }): CancelablePromise<MemberPydantic> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/members',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Many Member
     * @returns void
     * @throws ApiError
     */
    public static deleteManyMemberMembersDelete({
        filter = '{}',
    }: {
        filter?: string,
    }): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/members',
            query: {
                'filter': filter,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Member
     * @returns MemberPydantic Successful Response
     * @throws ApiError
     */
    public static getMemberMembersMemberIdGet({
        memberId,
    }: {
        memberId: number,
    }): CancelablePromise<MemberPydantic> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/members/{member_id}',
            path: {
                'member_id': memberId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Member
     * @returns MemberPydantic Successful Response
     * @throws ApiError
     */
    public static updateMemberMembersMemberIdPut({
        requestBody,
    }: {
        requestBody: MemberPydantic,
    }): CancelablePromise<MemberPydantic> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/members/{member_id}',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Member
     * @returns void
     * @throws ApiError
     */
    public static deleteMemberMembersMemberIdDelete({
        memberId,
    }: {
        memberId: number,
    }): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/members/{member_id}',
            path: {
                'member_id': memberId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Project Slots
     * @returns ProjectSlot Successful Response
     * @throws ApiError
     */
    public static getProjectSlotsProjectSlotsGet(): CancelablePromise<Array<ProjectSlot>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/project_slots',
        });
    }
    /**
     * Create Project Slot
     * @returns ProjectSlotCreateResponse Successful Response
     * @throws ApiError
     */
    public static createProjectSlotProjectSlotsPost({
        requestBody,
    }: {
        requestBody: ProjectSlotCreate,
    }): CancelablePromise<ProjectSlotCreateResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/project_slots',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Project Slot
     * @returns ProjectSlot Successful Response
     * @throws ApiError
     */
    public static updateProjectSlotProjectSlotsProjectSlotIdPut({
        projectSlotId,
        requestBody,
    }: {
        projectSlotId: number,
        requestBody: ProjectSlotCreate,
    }): CancelablePromise<ProjectSlot> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/project_slots/{project_slot_id}',
            path: {
                'project_slot_id': projectSlotId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Project Slot
     * @returns void
     * @throws ApiError
     */
    public static deleteProjectSlotProjectSlotsProjectSlotIdDelete({
        projectSlotId,
    }: {
        projectSlotId: number,
    }): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/project_slots/{project_slot_id}',
            path: {
                'project_slot_id': projectSlotId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Project Budgets
     * @returns ProjectBudget Successful Response
     * @throws ApiError
     */
    public static getProjectBudgetsProjectBudgetsGet(): CancelablePromise<Array<ProjectBudget>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/project_budgets',
        });
    }
    /**
     * Create Project Budget
     * @returns ProjectBudgetCreateResponse Successful Response
     * @throws ApiError
     */
    public static createProjectBudgetProjectBudgetsPost({
        requestBody,
    }: {
        requestBody: ProjectBudgetCreate,
    }): CancelablePromise<ProjectBudgetCreateResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/project_budgets',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Project Budget
     * @returns ProjectBudget Successful Response
     * @throws ApiError
     */
    public static updateProjectBudgetProjectBudgetsProjectBudgetIdPut({
        projectBudgetId,
        requestBody,
    }: {
        projectBudgetId: number,
        requestBody: ProjectBudgetCreate,
    }): CancelablePromise<ProjectBudget> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/project_budgets/{project_budget_id}',
            path: {
                'project_budget_id': projectBudgetId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Project Budget
     * @returns void
     * @throws ApiError
     */
    public static deleteProjectBudgetProjectBudgetsProjectBudgetIdDelete({
        projectBudgetId,
    }: {
        projectBudgetId: number,
    }): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/project_budgets/{project_budget_id}',
            path: {
                'project_budget_id': projectBudgetId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Project Member Assign
     * @returns ProjectMemberAssign Successful Response
     * @throws ApiError
     */
    public static getProjectMemberAssignProjectMemberAssignGet(): CancelablePromise<Array<ProjectMemberAssign>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/project_member_assign',
        });
    }
    /**
     * Create Project Member Assign
     * @returns ProjectMemberAssignCreateResponse Successful Response
     * @throws ApiError
     */
    public static createProjectMemberAssignProjectMemberAssignPost({
        requestBody,
    }: {
        requestBody: ProjectMemberAssignCreate,
    }): CancelablePromise<ProjectMemberAssignCreateResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/project_member_assign',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Project Member Assign
     * @returns ProjectMemberAssign Successful Response
     * @throws ApiError
     */
    public static updateProjectMemberAssignProjectMemberAssignProjectMemberAssignIdPut({
        projectMemberAssignId,
        requestBody,
    }: {
        projectMemberAssignId: number,
        requestBody: ProjectMemberAssignCreate,
    }): CancelablePromise<ProjectMemberAssign> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/project_member_assign/{project_member_assign_id}',
            path: {
                'project_member_assign_id': projectMemberAssignId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Project Member Assign
     * @returns void
     * @throws ApiError
     */
    public static deleteProjectMemberAssignProjectMemberAssignProjectMemberAssignIdDelete({
        projectMemberAssignId,
    }: {
        projectMemberAssignId: number,
    }): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/project_member_assign/{project_member_assign_id}',
            path: {
                'project_member_assign_id': projectMemberAssignId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Member Cost
     * @returns MemberCost Successful Response
     * @throws ApiError
     */
    public static getMemberCostMemberCostGet(): CancelablePromise<Array<MemberCost>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/member_cost',
        });
    }
    /**
     * Create Member Cost
     * @returns MemberCostCreateResponse Successful Response
     * @throws ApiError
     */
    public static createMemberCostMemberCostPost({
        requestBody,
    }: {
        requestBody: MemberCostCreate,
    }): CancelablePromise<MemberCostCreateResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/member_cost',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Member Cost
     * @returns MemberCost Successful Response
     * @throws ApiError
     */
    public static updateMemberCostMemberCostMemberCostIdPut({
        memberCostId,
        requestBody,
    }: {
        memberCostId: number,
        requestBody: MemberCostCreate,
    }): CancelablePromise<MemberCost> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/member_cost/{member_cost_id}',
            path: {
                'member_cost_id': memberCostId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Member Cost
     * @returns void
     * @throws ApiError
     */
    public static deleteMemberCostMemberCostMemberCostIdDelete({
        memberCostId,
    }: {
        memberCostId: number,
    }): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/member_cost/{member_cost_id}',
            path: {
                'member_cost_id': memberCostId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
