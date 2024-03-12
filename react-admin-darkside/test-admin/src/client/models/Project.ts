/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type Project = {
    name: string;
    /**
     * クライアントID
     */
    client_id: number;
    /**
     * プロジェクト開始日
     */
    start_date: string;
    /**
     * プロジェクト終了日
     */
    end_date?: (string | null);
    id: number;
    created_at: string;
    deleted_at: (string | null);
};

